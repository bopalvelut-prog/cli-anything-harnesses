import click
@click.group()
def cli(): pass
@cli.command()
def run(): click.echo('Semantic Kernel run')
@cli.command()
def plugins(): click.echo('Semantic Kernel plugins')
if __name__ == '__main__': cli()
