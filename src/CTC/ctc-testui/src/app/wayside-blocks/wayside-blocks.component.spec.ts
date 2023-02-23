import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WaysideBlocksComponent } from './wayside-blocks.component';

describe('WaysideBlocksComponent', () => {
  let component: WaysideBlocksComponent;
  let fixture: ComponentFixture<WaysideBlocksComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WaysideBlocksComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WaysideBlocksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
