(ql:quickload "cl-ppcre")

(defun parse-file (file)
  (let* ((lines (uiop:read-file-lines file))
         (arrivaltime (parse-integer (first lines)))
         (buslines (loop for busline in (cl-ppcre:split "," (second lines))
                         if (equal busline "x") collect busline
                           else collect (parse-integer busline))))
    (values buslines arrivaltime)))

(defun next-time-from-line (busline time)
  (* (ceiling (/ time busline)) busline))

(defun buslines-without-x (buslines)
  (remove-if (lambda (line) (equal line "x")) buslines))

(defun best-time-and-line (buslines time)
  (loop for bus-line in (buslines-without-x buslines)
        for bus-time = (next-time-from-line bus-line time)
        for (earliest-bus earliest-time) = (list bus-line bus-time)
          then (if (< bus-time earliest-time)
                   (list bus-line bus-time)
                   (list earliest-bus earliest-time))
        finally (return (list earliest-bus earliest-time))))

(defun part1 (&optional (filename "input"))
  (multiple-value-bind (buslines arrivaltime)
      (parse-file filename)
    (let* ((line-and-time (best-time-and-line buslines arrivaltime))
           (line (first line-and-time))
           (time (second line-and-time)))
      (* line (- time arrivaltime)))))

(defun enumerated-buslines (buslines)
  (loop for offset from 0
        for line in buslines
        when (numberp line)
          collect (list offset line)))

(defun first-occurrence (buslines)
  (loop for (offset line) in (enumerated-buslines buslines)
        for modulo = line then (* modulo line)
        and start = 0
              then (loop for number from start by modulo
                         until (eq (mod (+ number offset) line) 0)
                         finally (return number))
        finally (return start)))

(defun part2 (&optional (filename "input"))
  (first-occurrence (parse-file filename)))
