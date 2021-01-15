# LoanCalculator
Loan сalculator simulator (JetBrains Academy's project)

The script calculates the following loan parameters for annuity payment:
- loan principal
- number of periods
- annuity payment

It also can calculate all payments in case of differetiate payment.

All parameters are taken as command line arguments using argparse module

Examples of usage:
<pre>
python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6         # loan principal
python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8   # number of periods
python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10      # annuity payment
python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8          # differetiate payment
</pre>
