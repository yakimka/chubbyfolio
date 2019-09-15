const $ = django.jQuery;

class ExtendableError extends Error {
  constructor(message) {
    super(message);
    this.name = this.constructor.name;
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, this.constructor);
    } else {
      this.stack = (new Error(message)).stack;
    }
  }
}

class ParseError extends ExtendableError {
}

class ImageCropper {
  SELECTION_WIDTH = parseInt(600 / 3);
  SELECTION_HEIGHT = parseInt(675 / 3);
  COORDINATES_REGEXP = /^-?\d+,-?\d+$/;

  constructor(imgElement) {
    this.justCreated = true;
    this.isError = false;

    this.imgEl = imgElement;
    this.cropField = this.getCropField();
    this.imgWidth = this.imgEl.clientWidth;
    this.imgHeight = this.imgEl.clientHeight;
    const coords = this.initialCropCoordinates();
    this.x = coords.x;
    this.y = coords.y;
  }

  getCropField() {
    const trParent = $(this.imgEl).parents('tr');
    return trParent.find('.image-crop');
  }

  initialCropCoordinates() {
    try {
      return this.getCropCoordinatesFromHTML();
    } catch (e) {
      if (e instanceof ParseError) {
        this.isError = true;

        const centerCoords = this.getCenterCoordinates();
        this.setCropValueToHTML(centerCoords);

        return centerCoords;
      }
    }
  }

  getCropCoordinatesFromHTML() {
    const raw = this.getRawCropValue();
    return this.parseRawCropValue(raw);
  }

  getRawCropValue() {
    return this.cropField.val();
  }

  parseRawCropValue(val) {
    if (val === '') {
      return this.getCenterCoordinates();
    }
    if (this.COORDINATES_REGEXP.test(val)) {
      let coords = val.split(',');
      coords = {x: parseInt(coords[0]), y: parseInt(coords[1])};
      return this.percentsToCoordinates(coords);
    } else {
      throw new ParseError("Can't parse coordinates");
    }
  }

  getCenterCoordinates() {
    const xCenter = Math.round(this.imgWidth / 2 - this.SELECTION_WIDTH / 2);
    const yCenter = Math.round(this.imgHeight / 2 - this.SELECTION_HEIGHT / 2);

    return {x: xCenter, y: yCenter};
  }

  percentsToCoordinates(p) {
    const xCoord = Math.round(p.x * this.SELECTION_WIDTH / 100);
    const yCoord = Math.round(p.y * this.SELECTION_HEIGHT / 100);

    return {x: xCoord, y: yCoord}
  }

  setCropValueToHTMLIfNeeded = (coords) => {
    if (this.justCreated) {
      this.justCreated = false;
      return;
    }

    this.setCropValueToHTML(coords);
  };

  setCropValueToHTML = (coords) => {
    const c = this.coordinatesToPercents(coords);
    this.cropField.val(`${c.x},${c.y}`);
  };

  coordinatesToPercents(c) {
    const xPct = Math.round(c.x / this.SELECTION_WIDTH * 100);
    const yPct = Math.round(c.y / this.SELECTION_HEIGHT * 100);

    return {x: xPct, y: yPct}
  }

  getSelectAreaCoordinates() {
    const x = this.x;
    const y = this.y;
    const x2 = x + this.SELECTION_WIDTH;
    const y2 = y + this.SELECTION_HEIGHT;

    return [x, y, x2, y2];
  }
}

$(document).ready(function () {
  let errors = 0;
  let previewElements = document.querySelectorAll('.field-image img');

  for (let imgEl of previewElements) {
    try {
      const im = new ImageCropper(imgEl);

      $(imgEl).Jcrop({
        allowResize: false,
        allowSelect: false,
        setSelect: im.getSelectAreaCoordinates(),
        onSelect: im.setCropValueToHTMLIfNeeded
      });

      if (im.isError) {
        errors += 1;
      }
    } catch (e) {
      console.error(e);
    }
  }

  if (errors > 0) {
    console.error(`${errors} ошибок при попытке прочитать координаты`);
    alert('Возникла ошибка. Сохраните страницу чтобы попробовать исправить её.');
  }
});
