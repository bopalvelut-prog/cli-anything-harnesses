import click
@click.group()
def cli(): pass
@cli.command()
def generate(): click.echo('Stable Diffusion generate')
@cli.command()
def models(): click.echo('Stable Diffusion models')
if __name__ == '__main__': cli()
