(define (problem prac7)
(:domain tap1)
(:objects 
     L1 L2 L3 - location  ; L1, L2, L3 of type location
     PCK1 PCK2 - package  ; PCK1, PCK2 of type package
)

(:init
     (truck_at L1)        ; Truck initialised at Location 1
     (package_at PCK1 L2) ; Package 1 initialised at Location 2
     (package_at PCK2 L2) ; Package 2 initialised at Location 2
     (road L1 L2)         ; Road Location 1 -> Location 2
     (road L2 L1)         ; Both ways
     (road L1 L3)         ; Road Location 1 -> Location 3
     (road L3 L1)         ; Both ways
     )
     
(:goal (and
     (package_at PCK1 L3) ; Package 1 delivered to L3
     (package_at PCK2 L3) ; Package 2 delivered to L3
     )))