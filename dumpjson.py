#!/usr/bin/env python
import json


def main():
#classes
#classname
#field, data type
#method, parameter type, return type

#relationships
#tail class, tail class name, head class, head field
            
    ds = {
            "classes": [
                            {
                            "class": {
                                        "opts": 0,
                                        "name": "DSACircularQueue"
                                    },
                            "fields": {
                                        "opts": 0,
                                        "data": [
                                                ("objArray", "Object[]"),
                                                ("size", "int"),
                                                ("count", "int"),
                                                ("head", "int"),
                                                ("tail", "int")
                                                ]
                                        },
                            "methods": {
                                        "opts": {"makegetterssetters": False,
                                                "adddefaultmethods": False},
                                        "data": [
                                                ("alternate Constructor", "int", "void"),
                                                ("enqueue", "Object", "void"),
                                                ("dequeue", "void", "Object"),
                                                ("peek", "void", "Object"),
                                                ("isEmpty", "void", "boolean"),
                                                ("isFull", "void", "boolean"),
                                                ("getCount", "void", "int")
                                                ]
                                        },
                            }
                        ],
            "aggregation": [
                        ],
            "inheritance": [
                        ("DSAShufflingQueue", "dsashufflingqueue", "DSAQueue", "dsaqueue",),
                        ("DSACircularQueue", "dsacircularqueue", "DSAQueue", "dsaqueue",)
                        ],
            "composition": [
                        ],
            "dependency": [
                        ("DSAQueueTestHarness", "dsaqueuetestharness", "DSAShufflingQueue", "dsashufflingqueue",),
                        ("DSAQueueTestHarness", "dsaqueuetestharness", "DSACircularQueue", "dsacircularqueue",),
                        ("DSAStackTestHarness", "dsastacktestharness", "DSAStack", "dsastack",)
                        ]
        }
    
    for i in ds['classes']:
        if i['methods']['opts']['adddefaultmethods']:
            defaultmethods = [
                            ("toString", "", "String"),
                            ("equals", "Object inObj", "boolean")
                            ]
            i['methods']['data'].extend(defaultmethods)

    context = {
        'ds': ds
    }
    
    print(json.dumps(context))
    
#############################################################################

if __name__ == "__main__":
    main()
