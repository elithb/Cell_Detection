run("Subtract Background...", "rolling=5 light");
run("Bandpass Filter...", "filter_large=40 filter_small=2.5 suppress=None tolerance=5 autoscale saturate");
run("Auto Threshold", "method=Default");
run("Watershed");
run("Analyze Particles...", "size=13-Infinity pixel show=[Overlay Masks] clear summarize
