import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('CodeSandbox start')
@cli.command()
def deploy(): click.echo('CodeSandbox deploy')
if __name__ == '__main__': cli()
