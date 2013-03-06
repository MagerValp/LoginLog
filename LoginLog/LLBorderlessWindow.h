//
//  LLBorderlessWindow.h
//  LoginLog
//
//  Created by Pelle on 2013-03-05.
//  Copyright (c) 2013 Göteborgs universitet. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface LLBorderlessWindow : NSWindow

- (id) initWithContentRect:(NSRect)contentRect
                 styleMask:(unsigned int)aStyle
                   backing:(NSBackingStoreType)bufferingType
                     defer:(BOOL)flag;

@end
