import click
@click.group()
def cli(): pass
@cli.command()
def infer(): click.echo('ONNX infer')
@cli.command()
def models(): click.echo('ONNX models')
if __name__ == '__main__': cli()
