define({ "api": [
  {
    "type": "post",
    "url": "/classes",
    "title": "Add a new class",
    "version": "1.0.0",
    "name": "add_class",
    "group": "Classes",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The class's name.</p>"
          }
        ]
      }
    },
    "permission": [
      {
        "name": "user"
      }
    ],
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The class's id.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n  \"333\": {\n    \"name\": \"role::my_class\"\n  }\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X POST -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"role::my_class\" }' \\\nhttp://127.0.0.1:5000/api/v1/classes",
        "type": "curl"
      }
    ],
    "filename": "app/classes/routes.py",
    "groupTitle": "Classes"
  },
  {
    "type": "put",
    "url": "/classes/:id",
    "title": "Edit an existing class",
    "version": "1.0.0",
    "name": "edit_class",
    "permission": [
      {
        "name": "user"
      }
    ],
    "group": "Classes",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "success",
            "description": "<p>True if success</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "message",
            "description": "<p>A information message</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"message\": \"successfully modified\",\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X PUT -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"role::my_class\" }' \\\nhttp://127.0.0.1:5000/api/v1/classes/:id",
        "type": "curl"
      }
    ],
    "filename": "app/classes/routes.py",
    "groupTitle": "Classes"
  },
  {
    "type": "get",
    "url": "/classes/:id",
    "title": "Get a single class",
    "name": "get_class",
    "group": "Classes",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The class's id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The class's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The class's name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "hostgroups",
            "description": "<p>The class's hostgroups (by id)</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "insert_date",
            "description": "<p>The class's inserted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "update_date",
            "description": "<p>The class's updated date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "delete_date",
            "description": "<p>The class's deleted date</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"delete_date\": null,\n    \"hostgroups\": [\n      1\n    ],\n    \"id\": 1,\n    \"insert_date\": \"2017-04-11T13:55:40+00:00\",\n    \"name\": \"role::webserver\",\n    \"update_date\": null\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET http://127.0.0.1:5000/api/v1/classes/:id",
        "type": "curl"
      }
    ],
    "filename": "app/classes/routes.py",
    "groupTitle": "Classes"
  },
  {
    "type": "get",
    "url": "/classes",
    "title": "Get all classes",
    "name": "get_classes",
    "group": "Classes",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "limit",
            "defaultValue": "10",
            "description": "<p>(query parameter) Objects per page to display. Use limit=0 for disabling limit</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>(query parameter) Current page</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "filter",
            "description": "<p>(query parameter) Filter on name parameter (use * for searching any strings. Ex: <em>maclass</em>)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The class's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The class's name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "hostgroups",
            "description": "<p>The class's hostgroups (by id)</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "insert_date",
            "description": "<p>The class's inserted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "update_date",
            "description": "<p>The class's updated date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "delete_date",
            "description": "<p>The class's deleted date</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n[\n  {\n    \"delete_date\": null,\n    \"hostgroups\": [\n      1\n    ],\n    \"id\": 1,\n    \"insert_date\": \"2017-04-11T13:55:40+00:00\",\n    \"name\": \"role::webserver\",\n    \"update_date\": null\n  },\n  {\n    \"delete_date\": null,\n    \"hostgroups\": [\n      2\n    ],\n    \"id\": 2,\n    \"insert_date\": \"2017-04-11T13:55:25+00:00\",\n    \"name\": \"role::log\",\n    \"update_date\": null\n  }\n]",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/classes",
        "type": "curl"
      }
    ],
    "filename": "app/classes/routes.py",
    "groupTitle": "Classes"
  },
  {
    "type": "delete",
    "url": "/classes/:id",
    "title": "Delete a single class",
    "version": "1.0.0",
    "name": "rm_class",
    "permission": [
      {
        "name": "user"
      }
    ],
    "group": "Classes",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The class's id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "success",
            "description": "<p>Success (True if ok).</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>A success or error message.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"message\": \"<Class 'role::my_new_class'> deleted\",\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X DELETE http://127.0.0.1:5000/api/v1/classes/:id",
        "type": "curl"
      }
    ],
    "filename": "app/classes/routes.py",
    "groupTitle": "Classes"
  },
  {
    "type": "get",
    "url": "/enc/<node-name>",
    "title": "Get node informations (ENC)",
    "name": "get_enc",
    "group": "ENC",
    "permission": [
      {
        "name": "user"
      }
    ],
    "version": "1.0.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "node_name",
            "description": "<p>(uri parameter) The node's name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "output",
            "defaultValue": "yaml",
            "description": "<p>(query parameter) Output result. Avaiable methods : yaml / json</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The hostgroup's name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "insert_date",
            "description": "<p>The hostgroup's inserted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "update_date",
            "description": "<p>The hostgroup's updated date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "delete_date",
            "description": "<p>The hostgroup's deleted date</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\nclasses:\n- role::webserver\nenvironment: stable\nparameters:\n     hostgroup: my_hostgroup\n     puppenc_node_id: 2740\n     puppetmaster: ''",
          "type": "yaml"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -i http://127.0.0.1:5000/api/v1/enc/:node_name",
        "type": "curl"
      }
    ],
    "filename": "app/enc/routes.py",
    "groupTitle": "ENC"
  },
  {
    "type": "post",
    "url": "/environments",
    "title": "Add a new environment",
    "name": "add_environment",
    "group": "Environments",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>(json document) The environment's name.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The environment's id.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n  \"227\": {\n    \"name\": \"my_new_environment\"\n  }\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X POST -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"my_new_environment\" }' \\\nhttp://127.0.0.1:5000/api/v1/environments",
        "type": "curl"
      }
    ],
    "filename": "app/environments/routes.py",
    "groupTitle": "Environments"
  },
  {
    "type": "put",
    "url": "/environments/:id",
    "title": "Edit an existing environment",
    "name": "edit_environment",
    "group": "Environments",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>(uri parameter) The environment's id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "success",
            "description": "<p>True if success</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "message",
            "description": "<p>A information message</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"message\": \"successfully modified\",\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X PUT -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"my_new_environment\" }' \\\nhttp://127.0.0.1:5000/api/v1/environments/:id",
        "type": "curl"
      }
    ],
    "filename": "app/environments/routes.py",
    "groupTitle": "Environments"
  },
  {
    "type": "get",
    "url": "/environments/:id",
    "title": "Get a single environment",
    "name": "get_environment",
    "group": "Environments",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>(uri parameter) The environment's id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The environment's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The environment's name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "nodes",
            "description": "<p>The environment's nodes (by id)</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "insert_date",
            "description": "<p>The environment's inserted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "update_date",
            "description": "<p>The environment's updated date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "delete_date",
            "description": "<p>The environment's deleted date</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n  \"delete_date\": null,\n  \"id\": 2,\n  \"insert_date\": \"2017-04-11T13:56:03+00:00\",\n  \"name\": \"my_environment\",\n  \"nodes\": [\n    1498,\n    2817,\n    2818\n  ],\n  \"update_date\": null\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/environments/1",
        "type": "curl"
      }
    ],
    "filename": "app/environments/routes.py",
    "groupTitle": "Environments"
  },
  {
    "type": "get",
    "url": "/environments",
    "title": "Get all environments",
    "name": "get_environments",
    "group": "Environments",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "limit",
            "defaultValue": "10",
            "description": "<p>(query parameter) Objects per page to display. Use limit=0 for disabling limit</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>(query parameter) Current page</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "filter",
            "description": "<p>(query parameter) Filter on name parameter (use * for searching any strings. Ex: <em>maclass</em>)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The environment's id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The environment's name</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "nodes",
            "description": "<p>The environment's nodes (by id)</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "insert_date",
            "description": "<p>The environment's inserted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "update_date",
            "description": "<p>The environment's updated date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "delete_date",
            "description": "<p>The environment's deleted date</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n[\n  {\n    \"delete_date\": null,\n    \"id\": 1,\n    \"insert_date\": \"2017-04-11T13:56:03+00:00\",\n    \"name\": \"stable\",\n    \"nodes\": [\n      104,\n      2582,\n      2588\n    ],\n    \"update_date\": null\n  },\n  {\n    \"delete_date\": null,\n    \"id\": 2,\n    \"insert_date\": \"2017-04-11T13:56:04+00:00\",\n    \"name\": \"staging\",\n    \"nodes\": [\n      8,\n      34,\n      42\n    ],\n    \"update_date\": null\n  }\n]",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/environments",
        "type": "curl"
      }
    ],
    "filename": "app/environments/routes.py",
    "groupTitle": "Environments"
  },
  {
    "type": "delete",
    "url": "/environments/:id",
    "title": "Delete a single environment",
    "name": "rm_hostgorup",
    "group": "Environments",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>(uri parameter) The environment's id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "success",
            "description": "<p>Success (True if ok).</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>A success or error message.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"message\": \"<Environment 'my_new_environment'> deleted\",\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X DELETE http://127.0.0.1:5000/api/v1/environments/:id",
        "type": "curl"
      }
    ],
    "filename": "app/environments/routes.py",
    "groupTitle": "Environments"
  },
  {
    "type": "post",
    "url": "/hostgroups",
    "title": "Add a new hostgroup",
    "version": "1.0.0",
    "name": "add_hostgroup",
    "permission": [
      {
        "name": "user"
      }
    ],
    "group": "Hostgroups",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The hostgroup's name.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "class_id",
            "description": "<p>The related class id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The hostgroup's id.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n  \"227\": {\n    \"name\": \"my_new_hostgroup\"\n  }\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X POST -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"my_new_hostgroup\" }' \\\nhttp://127.0.0.1:5000/api/v1/hostgroups",
        "type": "curl"
      }
    ],
    "filename": "app/hostgroups/routes.py",
    "groupTitle": "Hostgroups"
  },
  {
    "type": "get",
    "url": "/hostgroups/<id>",
    "title": "Get a single hostgroup",
    "version": "1.0.0",
    "name": "get_hostgroup",
    "group": "Hostgroups",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The hostgroup's id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The hostgroup's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The hostgroup's name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "nodes",
            "description": "<p>The environment's nodes (by id)</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "insert_date",
            "description": "<p>The hostgroup's inserted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "update_date",
            "description": "<p>The hostgroup's updated date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "delete_date",
            "description": "<p>The hostgroup's deleted date</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n  \"class_id\": 10,\n  \"id\": 15,\n  \"insert_date\": \"2017-04-11T13:56:30+00:00\",\n  \"name\": \"my_hostgroup\",\n  \"nodes\": [\n    2164,\n    2165,\n    2166,\n    2167\n  ],\n  \"update_date\": \"2017-05-09T17:08:57+00:00\"\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET http://127.0.0.1:5000/api/v1/classes/:id",
        "type": "curl"
      }
    ],
    "filename": "app/hostgroups/routes.py",
    "groupTitle": "Hostgroups"
  },
  {
    "type": "get",
    "url": "/hostgroups",
    "title": "Get all hostgroups",
    "name": "get_hostgroups",
    "group": "Hostgroups",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "limit",
            "defaultValue": "10",
            "description": "<p>(query parameter) Objects per page to display. Use limit=0 for disabling limit</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>(query parameter) Current page</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "filter",
            "description": "<p>(query parameter) Filter on name parameter (use * for searching any strings. Ex: <em>maclass</em>)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The hostgroup's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The hostgroup's name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "nodes",
            "description": "<p>The environment's nodes (by id)</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "insert_date",
            "description": "<p>The hostgroup's inserted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "update_date",
            "description": "<p>The hostgroup's updated date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "delete_date",
            "description": "<p>The hostgroup's deleted date</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n[\n  {\n    \"class_id\": 1,\n    \"id\": 1,\n    \"insert_date\": \"2017-04-11T13:57:08+00:00\",\n    \"name\": \"webserver\",\n    \"nodes\": [\n      8,\n      42,\n      2661\n    ],\n    \"update_date\": null\n  },\n  {\n    \"class_id\": 2,\n    \"id\": 2,\n    \"insert_date\": \"2017-04-11T13:56:40+00:00\",\n    \"name\": \"logs\",\n    \"nodes\": [],\n    \"update_date\": null\n  }\n]",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/hostgroups",
        "type": "curl"
      }
    ],
    "filename": "app/hostgroups/routes.py",
    "groupTitle": "Hostgroups"
  },
  {
    "type": "put",
    "url": "/hostgroups/:id",
    "title": "Edit an hostgroup",
    "version": "1.0.0",
    "name": "put_hostgroup",
    "group": "Hostgroups",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The hostgroup's id.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The hostgroup's name.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "class_id",
            "description": "<p>The hostgroup's class_id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "success",
            "description": "<p>Success (True if ok).</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>A success or error message.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"message\": \"successfully modified\",\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X PUT -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"my_new_hostgroup\" }' \\\nhttp://127.0.0.1:5000/api/v1/hostgroups/1",
        "type": "curl"
      }
    ],
    "filename": "app/hostgroups/routes.py",
    "groupTitle": "Hostgroups"
  },
  {
    "type": "delete",
    "url": "/hostgroups/<id>",
    "title": "Delete a single hostgroup",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "name": "rm_hostgorup",
    "group": "Hostgroups",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The hostgroup's id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "success",
            "description": "<p>Success (True if ok).</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>A success or error message.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"message\": \"<Hostgroup 'my_new_hostgroup'> deleted\",\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X DELETE http://127.0.0.1:5000/api/v1/environments/:id",
        "type": "curl"
      }
    ],
    "filename": "app/hostgroups/routes.py",
    "groupTitle": "Hostgroups"
  },
  {
    "type": "post",
    "url": "/nodes",
    "title": "Add a new node",
    "version": "1.0.0",
    "name": "add_node",
    "permission": [
      {
        "name": "user"
      }
    ],
    "group": "Nodes",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The node's name.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The node's id.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n  \"2826\": {\n    \"name\": \"my_server\"\n  }\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X POST -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"my_server\", \"environment_id\":1 }' \\\nhttp://127.0.0.1:5000/api/v1/nodes",
        "type": "curl"
      }
    ],
    "filename": "app/nodes/routes.py",
    "groupTitle": "Nodes"
  },
  {
    "type": "post",
    "url": "/nodes/:id/variables",
    "title": "Assign an existing variable to a node",
    "version": "1.0.0",
    "name": "add_variable_to_node",
    "permission": [
      {
        "name": "user"
      }
    ],
    "description": "<p>The variable need to be created before.</p>",
    "group": "Nodes",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The node's id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "variable_id",
            "description": "<p>The variable's id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The node's id.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"message\": \"Successfully assign the variable <Variable 'name'> to the node <Node 'server01'>\",\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X POST -H \"Content-Type: application/json\" \\\n-d '{ \"variable_id\": 1 }' \\\nhttp://127.0.0.1:5000/api/v1/nodes/2/variables",
        "type": "curl"
      }
    ],
    "filename": "app/nodes/routes_variables.py",
    "groupTitle": "Nodes"
  },
  {
    "type": "get",
    "url": "/nodes/:id",
    "title": "Get a single node",
    "version": "1.0.0",
    "name": "get_node",
    "permission": [
      {
        "name": "user"
      }
    ],
    "group": "Nodes",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The node's id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The node's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The node's name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "insert_date",
            "description": "<p>The node's inserted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "update_date",
            "description": "<p>The node's updated date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "delete_date",
            "description": "<p>The node's deleted date</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n  \"active\": 1,\n  \"delete_date\": null,\n  \"environment_id\": 2,\n  \"hostgroup_id\": 36,\n  \"id\": 1,\n  \"insert_date\": \"2017-04-11T13:59:20+00:00\",\n  \"name\": \"server02\",\n  \"nodes_var\": [],\n  \"update_date\": null\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/nodes/1",
        "type": "curl"
      }
    ],
    "filename": "app/nodes/routes.py",
    "groupTitle": "Nodes"
  },
  {
    "type": "get",
    "url": "/nodes",
    "title": "Get all nodes",
    "name": "get_nodes",
    "group": "Nodes",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "limit",
            "defaultValue": "10",
            "description": "<p>(query parameter) Objects per page to display. Use limit=0 for disabling limit</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>(query parameter) Current page</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "filter",
            "description": "<p>(query parameter) Filter on name parameter (use * for searching any strings. Ex: <em>maclass</em>)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The node's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The node's name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "nodes_var",
            "description": "<p>The node's variables (by id)</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "insert_date",
            "description": "<p>The node's inserted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "update_date",
            "description": "<p>The node's updated date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "delete_date",
            "description": "<p>The node's deleted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "last_used",
            "description": "<p>The node's last use threw /nodes or /enc</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n[\n  {\n    \"active\": 1,\n    \"delete_date\": null,\n    \"environment_id\": 2,\n    \"hostgroup_id\": 1,\n    \"id\": 8,\n    \"insert_date\": \"2017-04-11T14:00:38+00:00\",\n    \"last_used\": \"2017-04-11T14:00:38+00:00\",\n    \"name\": \"server01\",\n    \"nodes_var\": [\n        1,\n        2\n    ],\n    \"update_date\": null\n  },\n  {\n    \"active\": 1,\n    \"delete_date\": null,\n    \"environment_id\": 2,\n    \"hostgroup_id\": 13,\n    \"id\": 34,\n    \"insert_date\": \"2017-04-11T13:59:20+00:00\",\n    \"name\": \"server02\",\n    \"nodes_var\": [],\n    \"update_date\": null\n  }\n]",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/nodes",
        "type": "curl"
      }
    ],
    "filename": "app/nodes/routes.py",
    "groupTitle": "Nodes"
  },
  {
    "type": "put",
    "url": "/nodes/:id",
    "title": "Edit a node",
    "version": "1.0.0",
    "name": "put_node",
    "group": "Nodes",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The node's id.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The node's name.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "environment_id",
            "description": "<p>The node's environment_id.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "hostgroup_id",
            "description": "<p>The node's hostgroup_id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "success",
            "description": "<p>Success (True if ok).</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>A success or error message.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"message\": \"successfully modified\",\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X PUT -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"my_new_server\" }' \\\nhttp://127.0.0.1:5000/api/v1/nodes/1",
        "type": "curl"
      }
    ],
    "filename": "app/nodes/routes.py",
    "groupTitle": "Nodes"
  },
  {
    "type": "delete",
    "url": "/nodes/:id",
    "title": "Delete a single node",
    "version": "1.0.0",
    "description": "<p>Delete will not delete the node from the database The flag active is set to 0, and delete_date is set to NOW()</p>",
    "permission": [
      {
        "name": "user"
      }
    ],
    "name": "rm_node",
    "group": "Nodes",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The node's id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "success",
            "description": "<p>Success (True if ok).</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>A success or error message.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X DELETE http://127.0.0.1:5000/api/v1/nodes/:id",
        "type": "curl"
      }
    ],
    "filename": "app/nodes/routes.py",
    "groupTitle": "Nodes"
  },
  {
    "type": "delete",
    "url": "/nodes/:id/variables",
    "title": "Unassign an existing variable to a node",
    "version": "1.0.0",
    "name": "rm_variable_to_node",
    "permission": [
      {
        "name": "user"
      }
    ],
    "group": "Nodes",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The node's id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "variable_id",
            "description": "<p>The variable's id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The node's id.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"message\": \"OK\",\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X DELETE -H \"Content-Type: application/json\" \\\n-d '{ \"variable_id\": 1 }' \\\nhttp://127.0.0.1:5000/api/v1/nodes/2/variables",
        "type": "curl"
      }
    ],
    "filename": "app/nodes/routes_variables.py",
    "groupTitle": "Nodes"
  },
  {
    "type": "get",
    "url": "/tokens",
    "title": "Get a token",
    "name": "get_token",
    "group": "Tokens",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>The token</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "duration",
            "description": "<p>The token's validity</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "duration",
            "defaultValue": "600",
            "description": "<p>(query parameter) Use a custom token duration</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET -u username:password \\\nhttp://127.0.0.1:5000/api/v1/tokens",
        "type": "curl"
      }
    ],
    "filename": "app/users/routes.py",
    "groupTitle": "Tokens"
  },
  {
    "type": "get",
    "url": "/users/<id>",
    "title": "Get a single user",
    "version": "1.0.0",
    "name": "get_user",
    "group": "Users",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The user's id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The user's name</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"name\": \"my_username\"\n}",
          "type": "json"
        }
      ]
    },
    "permission": [
      {
        "name": "public"
      }
    ],
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET -H \"Content-Type: application/json\" \\\nhttp://127.0.0.1:5000/api/v1/users/1",
        "type": "curl"
      }
    ],
    "filename": "app/users/routes.py",
    "groupTitle": "Users"
  },
  {
    "type": "post",
    "url": "/users",
    "title": "Create a user",
    "name": "post_user",
    "group": "Users",
    "version": "1.0.0",
    "permission": [
      {
        "name": "public"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>(json document) The user's name</p>"
          },
          {
            "group": "Parameter",
            "type": "Password",
            "optional": false,
            "field": "password",
            "description": "<p>(json document)The users's password</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The user's name</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"name\": \"my_username\"\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X POST -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"username\", \"password\": \"password\" }' \\\nhttp://127.0.0.1:5000/api/v1/users",
        "type": "curl"
      }
    ],
    "filename": "app/users/routes.py",
    "groupTitle": "Users"
  },
  {
    "type": "post",
    "url": "/variables",
    "title": "Add a new variable",
    "version": "1.0.0",
    "name": "add_variable",
    "group": "Variables",
    "description": "<p>Strings named true or false are automatically converted to Booleans. Strings in json format are automatically converted to objects.</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The variable's name.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "content",
            "description": "<p>The variable's content : you can use json here to specify arrays.</p>"
          }
        ]
      }
    },
    "permission": [
      {
        "name": "user"
      }
    ],
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The variable's id.</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Simple string",
        "content": "curl -X POST -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"my_variable\", \"content\": \"my_content\" }' \\\nhttp://127.0.0.1:5000/api/v1/variables",
        "type": "curl"
      },
      {
        "title": "JSON",
        "content": "curl -i -X POST -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"array\", \"content\":\"{\\\"ntp_servers\\\": [ \\\"ntp1\\\", \\\"ntp2\\\" ] }\" }' \\\nhttp://127.0.0.1:5000/api/v1/variables",
        "type": "curl"
      }
    ],
    "filename": "app/variables/routes.py",
    "groupTitle": "Variables"
  },
  {
    "type": "put",
    "url": "/variables/:id",
    "title": "Edit an existing variable",
    "version": "1.0.0",
    "name": "edit_variable",
    "permission": [
      {
        "name": "user"
      }
    ],
    "group": "Variables",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "success",
            "description": "<p>True if success</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "message",
            "description": "<p>A information message</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"message\": \"successfully modified\",\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X PUT -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"my_new_name\" }' \\\nhttp://127.0.0.1:5000/api/v1/variables/:id",
        "type": "curl"
      }
    ],
    "filename": "app/variables/routes.py",
    "groupTitle": "Variables"
  },
  {
    "type": "get",
    "url": "/variables/:id",
    "title": "Get a single variable",
    "name": "get_variable",
    "group": "Variables",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The variable's id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The variable's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The variable's name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "insert_date",
            "description": "<p>The variable's inserted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "update_date",
            "description": "<p>The variable's updated date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "delete_date",
            "description": "<p>The variable's deleted date</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET http://127.0.0.1:5000/api/v1/variables/:id",
        "type": "curl"
      }
    ],
    "filename": "app/variables/routes.py",
    "groupTitle": "Variables"
  },
  {
    "type": "get",
    "url": "/variables",
    "title": "Get all variables",
    "name": "get_variables",
    "group": "Variables",
    "version": "1.0.0",
    "permission": [
      {
        "name": "user"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "limit",
            "defaultValue": "10",
            "description": "<p>(query parameter) Objects per page to display. Use limit=0 for disabling limit</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>(query parameter) Current page</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "filter",
            "description": "<p>(query parameter) Filter on name parameter (use * for searching any strings. Ex: <em>mavariable</em>)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The variable's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The variable's name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "insert_date",
            "description": "<p>The variable's inserted date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "update_date",
            "description": "<p>The variable's updated date</p>"
          },
          {
            "group": "Success 200",
            "type": "Datetime",
            "optional": false,
            "field": "delete_date",
            "description": "<p>The variable's deleted date</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/variables",
        "type": "curl"
      }
    ],
    "filename": "app/variables/routes.py",
    "groupTitle": "Variables"
  },
  {
    "type": "delete",
    "url": "/variables/:id",
    "title": "Delete a single variable",
    "version": "1.0.0",
    "name": "rm_variable",
    "permission": [
      {
        "name": "user"
      }
    ],
    "group": "Variables",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The variable's id.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "success",
            "description": "<p>Success (True if ok).</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>A success or error message.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"message\": \"<Variable 'my_variable'> deleted\",\n    \"success\": true\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X DELETE http://127.0.0.1:5000/api/v1/variables/:id",
        "type": "curl"
      }
    ],
    "filename": "app/variables/routes.py",
    "groupTitle": "Variables"
  }
] });
