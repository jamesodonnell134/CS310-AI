; James O'Donnell (201711662)
; 26/3/2020
; University of Strathclyde, Glasgow
; CS310 - Foundations of Artificial Intelligence
; Practical 8
; Problem File - Part 2
; --------------------------------------------------------------------
; ANSWERS TO QUESTIONS:

; Does this plan seem sensible? :
;    Yes, as T1 only has 1 space, it is only able to pickup one package
;    at a time so must make several trips to and from the pickup and 
;    drop off locations until both packages are delivered.

; Is this plan optimal? :
;    Yes. This plan is optimal when adding the second truck as FF 
;    chooses the truck with the most spaces (truck T2 with 2) and 
;    fills these spaces which will therefore require less trips
;    to and from the pickup locations. T2 will complete delivery
;    in 1 "cycle".

(define (problem prac8-part2)
(:domain tap1-part2)
(:objects 
     L1 L2 L3 - location  ; L1, L2, L3 of type location
     PCK1 PCK2 - package  ; PCK1, PCK2 of type package
     T1 T2 - truck        ; T1, T2 of type truck
     S1 S2 S3 - space     ; S1, S2, S3 of type space
)

(:init
     (space_at T1 S1)     ; Initialising Space 1 in Truck 1
     (space_at T2 S2)     ; Initialising Space 2 in Truck 2
     (space_at T2 S3)     ; Initialising Space 3 in Truck 2
     
     (truck_at T2 L1)     ; Truck 2 initialised at Location 2
     (truck_at T1 L1)     ; Truck 1 initialised at Location 1
     
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
