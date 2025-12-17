(ns passport
  (:require [clojure.string :as str]))

(def input (slurp "input.txt"))

; byr (Birth Year)
; iyr (Issue Year)
; eyr (Expiration Year)
; hgt (Height)
; hcl (Hair Color)
; ecl (Eye Color)
; pid (Passport ID)
; cid (Country ID)

(def required [
  "byr"
  "iyr"
  "eyr"
  "hgt"
  "hcl"
  "ecl"
  "pid"
 ; "cid"
])

(def passports (str/split input #"\n\n"))

(defn valid? [passport]
  (let [fields (str/split passport #"\s")
        kvs (map #(str/split % #":") fields)
        pkeys (map first kvs)]
    (every? #((set pkeys) %) required)))

(println (count (filter valid? passports)))
