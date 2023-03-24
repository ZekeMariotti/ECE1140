import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CTCLinesComponent } from './ctc-lines.component';

describe('CTCLinesComponent', () => {
  let component: CTCLinesComponent;
  let fixture: ComponentFixture<CTCLinesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CTCLinesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CTCLinesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
