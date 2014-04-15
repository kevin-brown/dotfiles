;; 4 space tabbing
(setq-default indent-tabs-mode nil)
(setq tab-width 4)
(setq tab-stop-list '(4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80))

;; No backups
(setq backup-directory-alist
      `((".*" . ,temporary-file-directory)))
(setq auto-save-file-name-transforms
      `((".*" ,temporary-file-directory t)))

;; Show line-number in the mode line
(line-number-mode 1)

;; Get rid of yes-or-no questions - y or n is enough
(defalias 'yes-or-no-p 'y-or-n-p)

;; Always have the final newline
(setq-default require-final-newline 'ask)

(add-hook 'html-mode-hook
	  (lambda ()
          ;; Default indentation is usually 2 spaces, changing to 4.
          (set (make-local-variable 'sgml-basic-offset) 4)))

;; Show trailing whitespace
(setq-default show-trailing-whitespace t)

;; SCSS mode
(add-to-list 'load-path (expand-file-name "~/.emacs.d/plugins"))
(autoload 'scss-mode "scss-mode" "SCSS mode" t)
(add-to-list 'auto-mode-alist '("\\.scss\\'" . scss-mode))

;; Disable SCSS auto compile
(setq scss-compile-at-save 'nil)

;; YAML mode
(require 'yaml-mode)
(add-to-list 'auto-mode-alist '("\\.yml$" . yaml-mode))

;; Auto indent in YAML mode
(add-hook 'yaml-mode-hook
          '(lambda ()
             (define-key yaml-mode-map "\C-m" 'newline-and-indent)))

;; Handlebars mod
(require 'handlebars-mode)
(add-to-list 'auto-mode-alist '("\\.hbs\\'" . handlebars-mode))
