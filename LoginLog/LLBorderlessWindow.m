//
//  LLBorderlessWindow.m
//  LoginLog
//
//  Created by Pelle on 2013-03-05.
//  Copyright (c) 2013 Göteborgs universitet. All rights reserved.
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
