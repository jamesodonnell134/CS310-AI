; James O'Donnell (201711662)
; 26/3/2020
; University of Strathclyde, Glasgow
; CS310 - Foundations of Artificial Intelligence
; Practical 8
; Problem File - Part 3
; ------------------------------------------------------------------------
; ANSWERS TO QUESTIONS:

; How much fuel do you need to put at L3 to allow the problem to be solved?
;    4 canisters of fuel are required at L3

(define (problem prac8-part3)
(:domain tap1-part3)
(:objects 
     L1 L2 L3 - location           ; L1, L2, L3 of type location
     PCK1 PCK2 - package           ; PCK1, PCK2 of type package
     T1 T2 - truck                 ; T1, T2 of type truck
     S1 S2 S3 - space              ; S1, S2, S3 of type space
     C1 C2 C3 C4 C5 - canister     ; C1, CS, C3, C4, C5 of type cannister
)
(:init
     (canister_at L1 C1) ; Fuel canister 1 at Location 1
     (canister_at L3 C2) ; Fuel canister 2 at Location 3
     (canister_at L3 C3) ; Fuel canister 3 at Location 3
     (canister_at L3 C4) ; Fuel canister 4 at Location 3
     (canister_at L3 C5) ; Fuel canister 5 at Location 3

     (space_at T1 S1)    ; Initialising Space 1 in Truck 1
     (space_at T2 S2)    ; Initialising Space 2 in Truck 2
     (space_at T2 S3)    ; Initialising Space 3 in Truck 2
     
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
