# --- Part Two ---

Thanks in part to your analysis, the Elves have figured out a little bit about the issue. They now know that the problematic data path passes through both `dac` (a [digital-to-analog converter](https://en.wikipedia.org/wiki/Digital-to-analog_converter)) and `fft` (a device which performs a [fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)).

They're still not sure which specific path is the problem, and so they now need you to find every path from `svr` (the server rack) to `out`. However, the paths you find must all also visit both `dac` **and** `fft` (in any order).

For example:
```
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
```

This new list of devices contains many paths from `svr` to `out`:
```
svr,aaa,**fft**,ccc,ddd,hub,fff,ggg,out
svr,aaa,**fft**,ccc,ddd,hub,fff,hhh,out
svr,aaa,**fft**,ccc,eee,**dac**,fff,ggg,out
svr,aaa,**fft**,ccc,eee,**dac**,fff,hhh,out
svr,bbb,tty,ccc,ddd,hub,fff,ggg,out
svr,bbb,tty,ccc,ddd,hub,fff,hhh,out
svr,bbb,tty,ccc,eee,**dac**,fff,ggg,out
svr,bbb,tty,ccc,eee,**dac**,fff,hhh,out
```

However, only **`2`** paths from `svr` to `out` visit both `dac` and `fft`.

Find all of the paths that lead from `svr` to `out`. **How many of those paths visit both `dac` and `fft`?**
