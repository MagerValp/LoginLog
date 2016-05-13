//
//  LLBorderlessWindow.m
//  LoginLog
//
//  Created by Pelle on 2013-03-05.
//  Copyright 2013-2016 Per Olofsson, University of Gothenburg.
//

#import "LLBorderlessWindow.h"

@implementation LLBorderlessWindow

- (id) initWithContentRect:(NSRect)contentRect
                 styleMask:(unsigned int)aStyle
                   backing:(NSBackingStoreType)bufferingType
                     defer:(BOOL)flag
{
    self = [super initWithContentRect:contentRect
                            styleMask:NSBorderlessWindowMask
                              backing:bufferingType
                                defer:flag];
    return self;
}

@end
