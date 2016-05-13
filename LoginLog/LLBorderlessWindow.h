//
//  LLBorderlessWindow.h
//  LoginLog
//
//  Created by Pelle on 2013-03-05.
//  Copyright 2013-2016 Per Olofsson, University of Gothenburg.
//

#import <Cocoa/Cocoa.h>

@interface LLBorderlessWindow : NSWindow

- (id) initWithContentRect:(NSRect)contentRect
                 styleMask:(unsigned int)aStyle
                   backing:(NSBackingStoreType)bufferingType
                     defer:(BOOL)flag;

@end
