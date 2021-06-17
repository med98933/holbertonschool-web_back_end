export default class Currency {
  constructor(code, name) {
    if (typeof code === 'string' && typeof name === 'string') {
      this._code = code;
      this._name = name;
    } else {
      throw (TypeError('Attributes must be strings'));
    }
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('name must be a String');
    this._name = newName;
  }

  set code(newCode) {
    if (typeof newCode !== 'string') throw TypeError('code must be a String');
    this._code = newCode;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
