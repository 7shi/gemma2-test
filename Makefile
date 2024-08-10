SOURCES = breakdown-1.py breakdown-2.py breakdown-3.py breakdown-json.py \
		  inferno-1.py inferno-2.py hemingway.py proust.py
TARGETS = $(SOURCES:.py=.md)

all: $(TARGETS)

%.md: %.py
	python $<

clean:
	rm -f $(TARGETS)

.PHONY: all clean
