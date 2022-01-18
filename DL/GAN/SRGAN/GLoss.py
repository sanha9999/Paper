import torch
import torch.nn as nn
import torchvision.models as models

class GeneratorLoss(nn.Module):
    def __init__(self):
        super(GeneratorLoss, self).__init__()
        vgg = models.vgg16(pretrained=True)
        loss_network = nn.Sequential(*list(vgg.features)[:31]).eval()
        for param in loss_network.parameters():
            param.requires_grad = False
        self.loss_network = loss_network
        self.mse_loss = nn.MSELoss()
        self.l2_loss = L2Loss()
    def forward(self, out_labels, out_images, target_images):
        # adversarial loss
        adversarial_loss = torch.mean(1 - out_labels)
        # vgg loss
        vgg_loss = self.mse_loss(self.loss_network(out_images), self.loss_network(target_images))
        # pixel-wise loss
        pixel_loss = self.mse_loss(out_images, target_images)
        # regularization loss
        reg_loss = self.l2_loss(out_images)
        
        return pixel_loss + 0.001 * adversarial_loss + 0.006 * vgg_loss + 2e-8 * reg_loss

class L2Loss(nn.Module):
    def __init__(self, l2_loss_weight=1):
        super(L2Loss, self).__init__()
        self.l2_loss_weight = l2_loss_weight

    def forward(self, x):
        batch_size = x.size()[0]
        h_x = x.size()[2]
        w_x = x.size()[3]
        count_h = self.tensor_size(x[:, :, 1:, :])
        count_w = self.tensor_size(x[:, :, :, 1:])
        h_l2 = torch.pow((x[:, :, 1:, :] - x[:, :, :h_x - 1, :]), 2).sum()
        w_l2 = torch.pow((x[:, :, :, 1:] - x[:, :, :, w_x - 1:]), 2).sum()
        
        return self.l2_loss_weight * 2 * (h_l2 / count_h + w_l2 / count_w) / batch_size

    @staticmethod
    def tensor_size(t):
        return t.size()[1] * t.size()[2] * t.size()[3]
