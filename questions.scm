(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists


(define (helper_fn s index)
    (cond 
          
        ((null? s) nil)
        (else (cons (append (list index) (list (car s))) (helper_fn (cdr s) (+ index 1))))))
            
(define (enumerate s)
    
        
    (helper_fn s 0)
    
         

          )
  ; (append (apppend (list index) (list (car s))) (helper_fn (cdr s) (index+1))))
  
  
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to INORDER? and return
;; the merged lists.
(define (merge inorder? list1 list2)
  ; BEGIN PROBLEM 16
    (cond 
        
        
        ((and (null? list1) (null? list2)) ())
        ((null? list1 ) list2)
        ((null? list2) list1)
        ((= (car list1) (car list2)) (cons (append (list (car list1))) (merge inorder? (cdr list1) (list2))))
        ((equal? (inorder? (car list1) (car list2)) #t) (cons (append  (car list1)) (merge inorder? (cdr list1) list2)))
        ((equal? (inorder? (car list1) (car list2)) #f) (cons (append  (car list2)) (merge inorder? list1 (cdr list2))))
          
          
          ))
  
  
  ; END PROBLEM 16


;; Optional Problem 1

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           'replace-this-line
           ; END PROBLEM 17
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           'replace-this-line
           ; END PROBLEM 17
           ))
        (else
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )))



;; Problem 21 (optional)
;; Draw the hax image using turtle graphics.
(define (hax d k)
  ; BEGIN Question 21
  'replace-this-line
  )
  ; END Question 21