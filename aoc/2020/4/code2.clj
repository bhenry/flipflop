(ns passport
  (:require [clojure.string :as str]))

(def input (slurp "input.txt"))

; byr (Birth Year) - four digits; at least 1920 and at most 2002.
; iyr (Issue Year) - four digits; at least 2010 and at most 2020.
; eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
; hgt (Height) - a number followed by either cm or in:
; If cm, the number must be at least 150 and at most 193.
; If in, the number must be at least 59 and at most 76.
; hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
; ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
; pid (Passport ID) - a nine-digit number, including leading zeroes.
; cid (Country ID) - ignored, missing or not.

(defn valid-height? [h]
  (when h
		(let [in? (str/ends-with? h "in")
					cm? (str/ends-with? h "cm")
					height (apply str (butlast (butlast h)))]
			(when height
				(cond
					cm? (<= 150 (Integer. height) 193)
					in? (<= 59 (Integer. height) 76))))))

(def required {
  "byr" #(and (= 4 (count %)) (<= 1920 (Integer. %) 2002))
  "iyr" #(and (= 4 (count %)) (<= 2010 (Integer. %) 2020))
  "eyr" #(and (= 4 (count %)) (<= 2020 (Integer. %) 2030))
  "hgt" #(valid-height? %)
  "hcl" #(and %
	            (str/starts-with? % "#")
              (= 7 (count %))
              (every? #{\1 \2 \3 \4 \5 \6 \7 \8 \9 \0 \a \b \c \d \e \f} (drop 1 %)))
  "ecl" #{"amb" "blu" "gry" "grn" "hzl" "oth" "brn"}
  "pid" #(and (= 9 (count %))
	            (every? #{\1 \2 \3 \4 \5 \6 \7 \8 \9 \0} %))
})

(def passports (str/split input #"\n\n"))

(defn fields [p]
  (into {} (map #(str/split % #":") (str/split p #"\s"))))

(defn valid? [p]
  (let [fs (fields p)]
	  (every?
	    (fn [[k validator]]
	  	  (validator (fs k)))
	    required)))

(println (count (filter valid? passports)))
