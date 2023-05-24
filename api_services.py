import logging
import traceback


def get_args(req):
    logging.info('start /get_args')
    # -------------------------------- using values and json covers everything we need ---------------------------------------
    # args - The parsed URL parameters (the part in the URL after the question mark).
    # data - Contains the incoming request data as string in case it came with a mimetype Werkzeug does not handle.
    # files
    # form - The form parameters. By default an ImmutableMultiDict is returned from this function.
    # get_data
    # get_json
    # values - A werkzeug.datastructures.CombinedMultiDict that combines args and form.

    rv = {}
    logging.info('checking json')
    if req.is_json:
        logging.info('it\'s json')
        try:
            rv = req.get_json()
        except:
            logging.error('got exception on get_json(). (This can happen if the headers say it\'s JSON but the request doesn\'t have a body)')
    else:
        logging.info('it\'s not json')

    if not rv:
        try:
            logging.info('checking req.values')
            if req.values:
                logging.info('has req.values')
                rv = req.values
            else:
                logging.info('has no req.values')
        except BaseException:
            logging.error('got exception on req.values')
            logging.error(traceback.format_exc())
    logging.info('end /get_args')
    return rv