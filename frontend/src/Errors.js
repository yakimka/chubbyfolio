import Vue from 'vue';

class Errors {
  constructor() {
    this.errors = {};
  }

  has(field) {
    return Object.prototype.hasOwnProperty.call(this.errors, field);
  }

  any(fields = null) {
    if (fields) {
      for (const i in fields) {
        const hasField = Object.prototype.hasOwnProperty.call(this.errors, fields[i]);
        if (hasField) {
          return true;
        }
      }
    } else {
      return Object.keys(this.errors).length > 0;
    }
  }

  get(field) {
    if (this.errors[field]) {
      return this.errors[field][0];
    }
  }

  record(errors) {
    this.errors = errors;
  }

  recordByName(fieldName, message) {
    const error = {
      [fieldName]: { 0: message }
    };
    this.record(error);
  }

  clear(field) {
    if (field) {
      Vue.delete(this.errors, field);
      return;
    }
    this.errors = {};
  }
}

export default Errors;
