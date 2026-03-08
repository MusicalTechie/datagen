#!/usr/bin/env python3

from waitress import serve

serve(wsgiapp, listen='*:8080')
