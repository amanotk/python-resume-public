#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Gale-Shapley Matching Algorithm

 $Id$
"""
from __future__ import print_function

import os
import sys
import copy
import numpy as np
import json

#_DEBUG_ = True
_DEBUG_ = False

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


class Element:
    """Element for Gale-Shapley Algorithm
    """
    def __init__(self, nmax):
        # n    : number of available slots
        # pref : list of preference
        # slot : available slot
        self.pref = []
        self.slot = []
        self.n    = nmax

    def set_preference(self, pref):
        "set list of preference"
        self.pref = copy.copy(list(pref))

    def pop(self):
        """Pop a candidate from list of preference

        Return the top ranked candidate from the list of preference.
        None is returned if the list is empty.
        """
        if len(self.pref) > 0:
            c = self.pref[0]
            self.pref.remove(c)
        else:
            c = None
        return c

    def push(self, foo):
        """Push a candidate to list of slot

        If the candidate is in the list of preference, it tries to push it in
        the list of available slots. The slot is sorted according to the
        preference. If the number of available slots is not sufficient, the
        worst ranked candidate will be pushed out or rejected.

        Return tuple of (accepted, rejected) candidates or None if no one was
        rejected.
        """
        if self.pref.count(foo) != 0 and self.slot.count(foo) == 0:
            self.slot.append(foo)
            self.slot.sort(key=lambda x: self.pref.index(x))
            discarded = self.slot[self.n:]
            self.slot = self.slot[0:self.n]
        else:
            discarded = [foo]
        if len(discarded) == 0:
            return None
        elif len(discarded) == 1:
            return discarded[0]
        else:
            raise ValueError('Multiple values were pushed out from the slots')


def print_debug(*args, **kwargs):
    if _DEBUG_:
        print(*args, **kwargs)


def gsmatch(x, y):
    """Apply Gale-Shapley Matching Algorithm
    """
    nx = x.shape[0]
    ny = y.shape[0]
    xx = copy.deepcopy(x)
    yy = copy.deepcopy(y)
    # continue the loop while someone is in the list
    indices = list(range(nx))
    while len(indices) > 0:
        j = indices.pop()
        #
        # find candidate x
        #
        p = xx[j].pop()
        if p is None:
            # no candidate found
            continue
        print_debug('X[%2d] proposed to Y[%2d]' % (j, p))
        #
        # push candidate to an element of y
        #
        r = yy[p].push(j)
        if r is None:
            # proposed candidate was accepted
            print_debug('Y[%2d] accepted X[%2d]' % (p, j))
            xx[j].slot.append(p)
        elif r == j:
            # proposed candidate was rejected
            print_debug('Y[%2d] rejected X[%2d]' % (p, r))
            indices.append(r)
        else:
            # someone else was rejected
            print_debug('Y[%2d] accepted X[%2d] and rejected X[%2d]' % (p, j, r))
            indices.append(r)
            xx[j].slot.append(p)
            xx[r].slot.pop()
    #
    # pack results
    #
    results = [0]*(ny+1)
    for i in range(ny):
        results[i] = tuple(yy[i].slot)
    # get leftover
    i = ny
    results[i] = []
    for j in range(nx):
        if len(xx[j].slot) == 0:
            results[i].append(j)
    results[i] = tuple(results[i])
    return results


def read_assignment(fp):
    data = json.load(fp)

    deptid   = data['department']['deptid']
    deptname = data['department']['deptname']
    numdept  = data['department']['numdept']
    quota    = data['department']['quota']
    weight   = data['department']['weight']
    stdid    = data['student']['stdid']
    stdname  = data['student']['stdname']
    numstd   = data['student']['numstd']
    prefs    = data['student']['preference']
    score    = data['student']['score']

    # student and department elements
    x = np.empty((numstd,), object)
    y = np.empty((numdept,), object)

    quota  = np.array(quota)
    weight = np.array(weight)
    prefs  = np.array(prefs)
    score  = np.array(score)

    for i in range(numstd):
        x[i] = Element(1)
        pp   = prefs[i,prefs[i,:]>0] - 1
        x[i].set_preference(pp)

    for i in range(numdept):
        pts   = np.sum(weight[i,:][None,:]*score[:,:], axis=1)
        index = np.argsort(-pts)
        rank  = np.arange(numstd)[index]
        y[i]  = Element(quota[i])
        y[i].set_preference(rank)

    # problem definition
    problem = {
        'xid'  : stdid,
        'yid'  : deptid,
        'xname': stdname,
        'yname': deptname,
        'x'    : x,
        'y'    : y,
    }

    return problem


def get_assignment(problem, old=False):
    if old:
        return get_assignment_old(problem)
    else:
        return get_assignment_json(problem)


def get_assignment_old(problem):
    result  = problem['result']
    stdid   = problem['xid']
    deptid  = problem['yid']
    numdept = len(result) - 1
    s = ''
    for i in range(numdept):
        s += 'Department[%2d] : [' % (i+1)
        for student in result[i]:
            s += ' %3d' % (student+1,)
        s += ']\n'
    s += '\n'
    i = numdept
    s += 'Failed students:'
    for student in result[i]:
        s += ' %3d' % (student+1,)
    s+= '\n'
    return s


def get_assignment_json(problem):
    result   = problem['result']
    stdid    = np.array(problem['xid'])
    stdname  = np.array(problem['xname'])
    deptid   = np.array(problem['yid'])
    deptname = np.array(problem['yname'])
    numdept = len(result) - 1
    data = dict()
    for i in range(numdept):
        data[deptname[i]] = stdname[np.array(result[i])]
    i = numdept
    data['未決定者'] = stdname[np.array(result[i])]
    return json.dumps(data, indent=4, ensure_ascii=False, cls=NumpyEncoder)


def generate_testdata(**kwargs):
    """generate test data
    """
    numdept = kwargs['numdept']
    numsubj = kwargs['numsubj']
    numstd  = kwargs['numstd']
    average = kwargs['average']
    sigma   = kwargs['sigma']

    # student ids
    stdid   = np.arange(numstd) + 1
    stdname = np.array(['Name{:04d}'.format(i+1) for i in range(numstd)],
                       dtype=object)

    # score
    xmax  = 99.999
    xmin  =  0.001
    score = np.zeros((numstd, numsubj), dtype=np.float64)
    for i in range(numsubj):
        score[:,i] = np.random.normal(average[i], sigma[i], numstd)
    score[...] = np.where(score > xmax, 2*xmax - score, score)
    score[...] = np.where(score < xmin, 2*xmin - score, score)

    # preference
    npref = np.random.randint(1, numdept+1, numstd)
    prefs = np.argsort(np.random.rand(numstd, numdept), axis=-1) + 1
    index = np.arange(10)
    prefs[index[None,:] >= npref[:,None]] = -1

    return stdid, stdname, score, prefs


def generate_string_old(**kwargs):
    """return old format string for output
    """

    numdept = kwargs['numdept']
    numsubj = kwargs['numsubj']
    numstd  = kwargs['numstd']
    quota   = kwargs['quota']
    deptid  = kwargs['deptid']
    weight  = kwargs['weight']
    stdid   = kwargs['stdid']
    score   = kwargs['score']
    prefs   = kwargs['prefs']

    s = ''

    ### output department data
    s += '{:3d}'.format(numdept)
    s += '{:3d}'.format(numsubj)
    s += '\n\n'

    for i in range(numdept):
        s += '{:3d}  '.format(quota[i])
        for j in range(numsubj):
            s += '{:5.2f}'.format(weight[i,j])
        s += '\n'
    s += '\n\n\n'

    ### output student data
    s += '{:d}'.format(numstd)
    s += '\n\n'
    for i in range(numstd):
        for j in range(numsubj):
            s += '{:5.2f}  '.format(score[i,j])
        for j in range(numdept):
            s += ' {:4d}'.format(prefs[i,j])
        s += '\n'

    return s


def generate_string_json(**kwargs):
    """return JSON string for output
    """
    numdept  = kwargs['numdept']
    numsubj  = kwargs['numsubj']
    numstd   = kwargs['numstd']
    quota    = kwargs['quota']
    deptid   = kwargs['deptid']
    deptname = kwargs['deptname']
    weight   = kwargs['weight']
    stdid    = kwargs['stdid']
    stdname  = kwargs['stdname']
    score    = kwargs['score']
    prefs    = kwargs['prefs']

    ### department
    department = {
        'numdept'  : numdept,
        'deptid'   : deptid,
        'deptname' : deptname,
        'quota'    : quota,
        'numsubj'  : numsubj,
        'weight'   : weight,
    }

    ### student
    student = {
        'numstd'     : numstd,
        'stdid'      : stdid,
        'stdname'    : stdname,
        'score'      : score,
        'preference' : prefs,
    }

    data = {
        'department' : department,
        'student'    : student,
    }
    return json.dumps(data, indent=4, ensure_ascii=False, cls=NumpyEncoder)


def generate_assignment(fn, small=False, old=False):
    if small:
        numdept = 10
        numstd  = 40
        numsubj = 3
        quota   = np.array([4, 2, 7, 1, 3, 2, 4, 2, 1, 2], np.int32)
        deptid   = np.arange(numdept) + 1
        deptname = np.array(['数学科',
                             '情報科学科',
                             '物理学科',
                             '天文学科',
                             '地球惑星物理学科',
                             '地球惑星環境学科',
                             '化学科',
                             '生物化学科',
                             '生物学科',
                             '生物情報学科'])
        weight  = np.array(
            [[0.25, 0.25, 0.50],
             [0.50, 0.25, 0.25],
             [0.50, 0.40, 0.10],
             [0.33, 0.33, 0.34],
             [0.50, 0.20, 0.30],
             [0.50, 0.30, 0.20],
             [0.40, 0.30, 0.40],
             [0.33, 0.33, 0.34],
             [0.40, 0.40, 0.20],
             [0.33, 0.33, 0.34]])
        average = np.array([50.0, 40.0, 60.0])
        sigma   = np.array([25.0, 20.0, 10.0])
    else:
        numdept  = 10
        numstd   = 310
        numsubj  = 5
        quota    = np.array([45, 28, 70, 9, 32, 20, 45, 20, 10, 20], np.int32)
        deptid   = np.arange(numdept) + 1
        deptname = np.array(['数学科',
                             '情報科学科',
                             '物理学科',
                             '天文学科',
                             '地球惑星物理学科',
                             '地球惑星環境学科',
                             '化学科',
                             '生物化学科',
                             '生物学科',
                             '生物情報学科'])
        weight  = np.array(
            [[0.60, 0.10, 0.10, 0.10, 0.10],
             [0.50, 0.15, 0.10, 0.10, 0.15],
             [0.20, 0.50, 0.05, 0.05, 0.20],
             [0.20, 0.40, 0.10, 0.10, 0.20],
             [0.20, 0.40, 0.10, 0.10, 0.20],
             [0.20, 0.20, 0.20, 0.20, 0.20],
             [0.10, 0.10, 0.50, 0.10, 0.20],
             [0.10, 0.10, 0.30, 0.30, 0.20],
             [0.20, 0.15, 0.15, 0.30, 0.20],
             [0.15, 0.15, 0.20, 0.30, 0.20]])
        average = np.array([40.0, 50.0, 60.0, 55.0, 60.0])
        sigma   = np.array([25.0, 20.0, 15.0, 10.0, 15.0])


    kwargs = {
        'numdept'  : numdept,
        'deptid'   : deptid,
        'deptname' : deptname,
        'quota'    : quota,
        'numsubj'  : numsubj,
        'weight'   : weight,
        'numstd'   : numstd,
        'average'  : average,
        'sigma'    : sigma,
    }

    # generate test data
    stdid, stdname, score, prefs = generate_testdata(**kwargs)

    kwargs['stdid']   = stdid
    kwargs['stdname'] = stdname
    kwargs['score']   = score
    kwargs['prefs']   = prefs

    # json output
    with open(fn, 'w') as fp:
        fp.write(generate_string_json(**kwargs))

    # output old style if requested
    if old:
        with open(fn + '.old', 'w') as fp:
            fp.write(generate_string_old(**kwargs))


if __name__ == '__main__':
    # for command line options
    from optparse import OptionParser
    usage = \
"""\
Usage: %prog [options] filename

By default, read the given file and apply the Gale-Shapley Matching Algorithm
for the problem of students assignment into departments.
If "-g" option is given, test data will be written out into the file.
marriage problem, instead.
"""
    parser = OptionParser(usage=usage)
    parser.add_option('-g', '--generate-test', dest='test', default=False,
                      action='store_true', help='generate test data file')
    parser.add_option('-o', '--old', dest='old', default=False,
                      action='store_true', help='old style input/output')
    parser.add_option('-s', '--small', dest='small', default=False,
                      action='store_true', help='generate small dataset')

    opts, args = parser.parse_args()
    if len(args) != 1:
        print('Error: filename must be given with the first command line argument')
        print('')
        parser.print_help()
        sys.exit(-1)
    fn = args[0]

    # student assignment
    if opts.test:
        # generate test data file
        generate_assignment(fn, opts.small, opts.old)
    else:
        # read data and analyze
        with open(fn, 'r') as fp:
            problem = read_assignment(fp)
        problem['result'] = gsmatch(problem['x'], problem['y'])
        # print result
        print(get_assignment(problem, opts.old))
