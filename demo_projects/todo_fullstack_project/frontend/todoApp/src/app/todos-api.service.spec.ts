import { TestBed } from '@angular/core/testing';

import { TodosAPIService } from './todos-api.service';

describe('TodosAPIService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TodosAPIService = TestBed.get(TodosAPIService);
    expect(service).toBeTruthy();
  });
});
