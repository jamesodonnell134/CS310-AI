; James O'Donnell (201711662)
; 26/3/2020
; University of Strathclyde, Glasgow
; CS310 - Foundations of Artificial Intelligence
; Practical 8
; Domain File - Part 2

; Answers to questions in problem file:

(define (domain tap1-part2)

(:predicates
	(road ?l1 - location ?l2 - location)
	(package_at ?p - package ?l - location)
	(truck_at ?t - truck ?l - location)
	(carrying ?t - truck ?p - package)
	(space_at ?t - truck ?s - space)
	)

(:types
	package, location, truck, space - object
)

(:action move
	:parameters (?t - truck ?l1 ?l2 - location)
	:precondition (and(road ?l1 ?l2)(truck_at ?t ?l1))
	:effect(and(not (truck_at ?t ?l1))(truck_at ?t ?l2)))

(:action load
	:parameters (?l - location ?p - package ?t - truck ?s - space)
	:precondition (and(package_at ?p ?l)(truck_at ?t ?l)(space_at ?t ?s))
	:effect(and(not (package_at ?p ?l))(not(space_at ?t ?s))(carrying ?t ?p)))

(:action unload
	:parameters (?l - location ?p - package ?t - truck ?s - space)
	:precondition (and(carrying ?t ?p)(truck_at ?t ?l))
	:effect(and(not (carrying ?t ?p))(package_at ?p ?l)(space_at ?t ?s)))

)
