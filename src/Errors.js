import Vue from 'vue';

class Errors {
  constructor() {
    this.errors = {};
  }

  has(field) {
    return this.errors.hasOwnProperty(field);
  }

  any() {
    if (this.errors['error']) {
      return Object.keys(this.errors).length > 1;
    }
    return Object.keys(this.errors).length > 0;
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
    let error = {
      [fieldName]: {'0': message}
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
