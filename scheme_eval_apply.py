import sys

from pair import *
from scheme_utils import *
from math import *

from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############



def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms

    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:


        # BEGIN PROBLEM 3
        # evalautea what expr.first is (the operator).
        # return scheme_apply(expr.first, REST_OF_SCHEME_list, env)
        copy_of_expr = expr
        operator = copy_of_expr.first
        operator_eval = scheme_eval(operator, env, _=None)

        rest = expr.rest

        rest_evaluated = rest.map(lambda b_value: scheme_eval(b_value, env))

        return scheme_apply(operator_eval, rest_evaluated, env)


        # END PROBLEM 3

        #new_scheme_list = Pair.map(expr_copy, f)
def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2


        #1.) convert Pair list into python list,  if env exists add to end of lsit




        python_list = []

        if args != nil:
            while args.rest:
                python_list.append(args.first)
                args = args.rest


            python_list.append(args.first)

        if procedure.expect_env:

            python_list.append(env)
        try:
            return procedure.py_func(*python_list)

        except TypeError:
            raise SchemeError('incorrect number of arguments')

        if args == nil:
            if python_list:
                return procedure.py_func(python_list[0])
            return procedure.py_func()



        # END PROBLEM 2
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        #procedure is already a lambda OBJECT!

        #frame = Frame(env)  #in case it doesnt work later on, change env with procedure.env
        #frame2 = Frame(procedure.env)
                 #procedure2 = procedure


                 #new_env = procedure2.env.make_child_frame(procedure2.formals, args)
                 #return eval_all(procedure2.body, new_env)
        #env = procedure.env
       # frame = Frame(procedure.env)


        new_env = procedure.env.make_child_frame(procedure.formals, args)

        return eval_all(procedure.body, new_env)
        #frame = Frame(env)

       # new_frame = Frame.make_child_frame(frame, procedure.formals, args)

        #print("DEBUG:", new_frame)
        #print("DEBUG:", procedure.env)
        #print("DEBUG:", frame)

        #return eval_all(procedure.body, new_frame)

        # END PROBLEM 9


    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        # the parent of the new call frame is the environment in which that call expression was evaluated.

        frame = Frame(env)

        new_env = frame.make_child_frame(procedure.formals, args)

        return eval_all(procedure.body, new_env)


        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    if expressions == nil:
        return None

    while expressions.rest:
        scheme_eval(expressions.first, env)
        expressions = expressions.rest

    return scheme_eval(expressions.first, env)

    # END PROBLEM 6


##################
# Tail Recursion #
##################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val


def optimize_tail_calls(unoptimized_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)

        result = Unevaluated(expr, env)
        # BEGIN PROBLEM EC
       # if not tail:  #not in a tail context, so we have to make it into a tail context?

        #if tail:   # in a  tail context so we should be free to just use complete apply?

        """ ur code here """

    # END PROBLEM EC
    return optimized_eval


################################################################
# Uncomment the following line to apply tail call optimization #
################################################################
# scheme_eval = optimize_tail_calls(scheme_eval)
