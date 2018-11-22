(defun rebalance (n p v)
  "given: 
    n (new amount to add to accounts)
    p (list of percentages of total that each account should be)
    v (list of current values of each account)
  return: list of amounts each account must change by to satisfy p "
  (let ((total (+ n (apply '+ v))))
    (map 'list #'(lambda (x y)
                  (- (* (float (/ x 100)) total) y))
         p
         v)))
