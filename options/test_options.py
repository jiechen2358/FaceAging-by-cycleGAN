from .base_options import BaseOptions


class TestOptions(BaseOptions):
    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)
        parser.add_argument('--ntest', type=int, default=float("inf"), help='# of test examples.')
        parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
        parser.add_argument('--aspect_ratio', type=float, default=1.0, help='aspect ratio of result images')
        parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
        #  Dropout and Batchnorm has different behavioir during training and test.
        parser.add_argument('--eval', action='store_true', help='use eval mode during test time.')
        parser.add_argument('--num_test', type=int, default=50, help='how many test images to run')

        parser.set_defaults(model='test')
        # To avoid cropping, the loadSize should be the same as fineSize
        parser.set_defaults(loadSize=parser.get_default('fineSize'))

        parser.add_argument('--use_pretrained_model', action='store_true', help='whether we should use pretrained model')
        parser.add_argument('--pretrained_model_name', type=str, default='', help='name of the pretrained model we want to use for transfer learning, e.g. orange2apple')
        parser.add_argument('--pretrained_model_subname', type=str, default='', help='name of the sub models (comma delimited) we want to use for transfer learning, e.g. GA,GB')
        parser.add_argument('--pretrained_model_epoch', type=int, default=1, help='epoch of the pretrained model we want to use for transfer learning')
        parser.add_argument('--G_A_freeze_layer', type=int, default=0, help='freeze these many initial layers (inclusive) of G_A network during training')
        parser.add_argument('--G_B_freeze_layer', type=int, default=0, help='freeze these many initial layers (inclusive) of G_B network during training')
        parser.add_argument('--D_A_freeze_layer', type=int, default=0, help='freeze these many initial layers (inclusive) of D_A network during training')
        parser.add_argument('--D_B_freeze_layer', type=int, default=0, help='freeze these many initial layers (inclusive) of D_B network during training')

        self.isTrain = False
        return parser
