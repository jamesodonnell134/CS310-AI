(define (domain tap1)

(:predicates
	(road ?l1 - location ?l2 - location)
	(package_at ?p - package ?l - location)
	(truck_at ?l - location)
	(carrying ?p - package))

(:types
	package - object
	location - object
)

(:action move
	:parameters (?l1 ?l2 - location)
	:precondition (and(road ?l1 ?l2)(truck_at ?l1))
	:effect(and(not (truck_at ?l1))(truck_at ?l2)))

(:action load
	:parameters (?l - location ?p - package)
	:precondition (and(package_at ?p ?l)(truck_at ?l))
	:effect(and(not (package_at ?p ?l))(carrying ?p)))

(:action unload
	:parameters (?l - location ?p - package)
	:precondition (and(carrying ?p)(truck_at ?l))
	:effect(and(not (carrying ?p))(package_at ?p ?l)))

)