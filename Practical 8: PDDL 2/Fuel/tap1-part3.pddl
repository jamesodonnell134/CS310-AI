; James O'Donnell (201711662)
; 26/3/2020
; University of Strathclyde, Glasgow
; CS310 - Foundations of Artificial Intelligence
; Practical 8
; Domain File - Part 3

; Answers to questions in problem file


(define (domain tap1-part3)

(:predicates
	(road ?l1 - location ?l2 - location)
	(package_at ?p - package ?l - location)
	(truck_at ?t - truck ?l - location)
	(carrying ?t - truck ?p - package)
	(space_at ?t - truck ?s - space)
	(canister_at ?l - location ?c - canister)
	(fuel_in ?t - truck ?c - canister)

	)

(:types
	package, location, truck, space, canister - object
)

(:action move
	:parameters (?t - truck ?l1 ?l2 - location ?c - canister)
	:precondition (and(road ?l1 ?l2)(truck_at ?t ?l1)(fuel_in ?t ?c))
	:effect(and(not (truck_at ?t ?l1))(not(fuel_in ?t ?c))(truck_at ?t ?l2)))

(:action load
	:parameters (?l - location ?p - package ?t - truck ?s - space)
	:precondition (and(package_at ?p ?l)(truck_at ?t ?l)(space_at ?t ?s))
	:effect(and(not (package_at ?p ?l))(not(space_at ?t ?s))(carrying ?t ?p)))

(:action unload
	:parameters (?l - location ?p - package ?t - truck ?s - space)
	:precondition (and(carrying ?t ?p)(truck_at ?t ?l))
	:effect(and(not (carrying ?t ?p))(package_at ?p ?l)(space_at ?t ?s)))

(:action refuel
	:parameters (?l - location ?c - canister ?t - truck)
	:precondition (and(canister_at ?l ?c)(truck_at ?t ?l))
	:effect(and(not (canister_at ?l ?c))(fuel_in ?t ?c)))

)
