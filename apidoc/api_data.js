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
      }
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
    "url": "/classes/<id>",
    "title": "Edit an existing class",
    "version": "1.0.0",
    "name": "edit_class",
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
      }
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X PUT -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"role::my_class\" }' \\\nhttp://127.0.0.1:5000/api/v1/classes/<id>",
        "type": "curl"
      }
    ],
    "filename": "app/classes/routes.py",
    "groupTitle": "Classes"
  },
  {
    "type": "get",
    "url": "/classes/<id>",
    "title": "Get a single class",
    "version": "1.0.0",
    "name": "get_class",
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
      }
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET http://127.0.0.1:5000/api/v1/classes/<id>",
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
    "version": "1.0.0",
    "name": "get_classes",
    "group": "Classes",
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
      }
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X GET http://127.0.0.1:5000/api/v1/classes",
        "type": "curl"
      }
    ],
    "filename": "app/classes/routes.py",
    "groupTitle": "Classes"
  },
  {
    "type": "delete",
    "url": "/classes/<id>",
    "title": "Delete a single class",
    "version": "1.0.0",
    "name": "rm_class",
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
      }
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X DELETE http://127.0.0.1:5000/api/v1/classes/<id>",
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
    "version": "1.0.0",
    "name": "get_enc",
    "group": "ENC",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "node_name",
            "description": "<p>The node's name</p>"
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
      }
    },
    "filename": "app/enc/routes.py",
    "groupTitle": "ENC"
  },
  {
    "type": "post",
    "url": "/environments",
    "title": "Add a new environment",
    "version": "1.0.0",
    "name": "add_environment",
    "group": "Environments",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The environment's name.</p>"
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
      }
    },
    "filename": "app/environments/routes.py",
    "groupTitle": "Environments"
  },
  {
    "type": "put",
    "url": "/environments/<id>",
    "title": "Edit an existing environment",
    "version": "1.0.0",
    "name": "edit_environment",
    "group": "Environments",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The environment's name.</p>"
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
      }
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X PUT -H \"Content-Type: application/json\" \\\n-d '{ \"name\": \"my_new_environment\" }' \\\nhttp://127.0.0.1:5000/api/v1/environments/<id>",
        "type": "curl"
      }
    ],
    "filename": "app/environments/routes.py",
    "groupTitle": "Environments"
  },
  {
    "type": "get",
    "url": "/environments/<id>",
    "title": "Get a single environment",
    "version": "1.0.0",
    "name": "get_environment",
    "group": "Environments",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The environment's id.</p>"
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
      }
    },
    "filename": "app/environments/routes.py",
    "groupTitle": "Environments"
  },
  {
    "type": "get",
    "url": "/environments",
    "title": "Get all environments",
    "version": "1.0.0",
    "name": "get_environments",
    "group": "Environments",
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
      }
    },
    "filename": "app/environments/routes.py",
    "groupTitle": "Environments"
  },
  {
    "type": "delete",
    "url": "/environments/<id>",
    "title": "Delete a single environment",
    "version": "1.0.0",
    "name": "rm_hostgorup",
    "group": "Environments",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The environment's id.</p>"
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
      }
    },
    "filename": "app/environments/routes.py",
    "groupTitle": "Environments"
  },
  {
    "type": "post",
    "url": "/hostgroups",
    "title": "Add a new hostgroup",
    "version": "1.0.0",
    "name": "add_hostgroup",
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
      }
    },
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
      }
    },
    "filename": "app/hostgroups/routes.py",
    "groupTitle": "Hostgroups"
  },
  {
    "type": "get",
    "url": "/hostgroups",
    "title": "Get all hostgroups",
    "version": "1.0.0",
    "name": "get_hostgroups",
    "group": "Hostgroups",
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
      }
    },
    "filename": "app/hostgroups/routes.py",
    "groupTitle": "Hostgroups"
  },
  {
    "type": "delete",
    "url": "/hostgroups/<id>",
    "title": "Delete a single hostgroup",
    "version": "1.0.0",
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
      }
    },
    "filename": "app/hostgroups/routes.py",
    "groupTitle": "Hostgroups"
  },
  {
    "type": "post",
    "url": "/nodes",
    "title": "Add a new node",
    "version": "1.0.0",
    "name": "add_node",
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
      }
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
    "type": "get",
    "url": "/nodes/<id>",
    "title": "Get a single node",
    "version": "1.0.0",
    "name": "get_node",
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
      }
    },
    "filename": "app/nodes/routes.py",
    "groupTitle": "Nodes"
  },
  {
    "type": "get",
    "url": "/nodes",
    "title": "Get all nodes",
    "version": "1.0.0",
    "name": "get_nodes",
    "group": "Nodes",
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
      }
    },
    "filename": "app/nodes/routes.py",
    "groupTitle": "Nodes"
  },
  {
    "type": "put",
    "url": "/nodes/<id>",
    "title": "Edit a node",
    "version": "1.0.0",
    "name": "put_node",
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
      }
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
    "url": "/nodes/<id>",
    "title": "Delete a single node",
    "version": "1.0.0",
    "description": "<p>Delete will not delete the node from the database The flag active is set to 0, and delete_date is set to NOW()</p>",
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
      }
    },
    "examples": [
      {
        "title": "Example usage :",
        "content": "curl -X DELETE http://127.0.0.1:5000/api/v1/nodes/<id>",
        "type": "curl"
      }
    ],
    "filename": "app/nodes/routes.py",
    "groupTitle": "Nodes"
  }
] });
