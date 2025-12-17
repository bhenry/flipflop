(ns trees)

(def land (slurp "trees.txt"))
(def lanes (clojure.string/split-lines land))

(def tree_count (atom 0))

(doseq [[i row] (map-indexed vector lanes)]
  (when (= \# (get row (mod (* i 3) (count row))))
    (swap! tree_count inc)))

(print @tree_count)
