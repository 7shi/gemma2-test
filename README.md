# gemma2-test

Gemma 2 test. Mainly translation.

# Log

The `script` command outputs standard output to a file, `tr` removes CR from CRLF, and `head` and `tail` remove the header and footer.

```
script -c "python xxxx.py"
tr -d '\r' < typescript | tail -n +3 | head -n -2 > xxxx.md
```

# CPU

The measurements were taken using the following CPU:

* Intel(R) Core(TM) i5-3320M (2.6GHz)
