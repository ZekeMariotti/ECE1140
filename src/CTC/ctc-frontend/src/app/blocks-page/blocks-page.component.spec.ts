import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BlocksPageComponent } from './blocks-page.component';

describe('BlocksPageComponent', () => {
  let component: BlocksPageComponent;
  let fixture: ComponentFixture<BlocksPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BlocksPageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BlocksPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
