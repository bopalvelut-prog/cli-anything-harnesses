import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('linter running')
@cli.command()
def start(): click.echo('linter started')
if __name__ == '__main__': cli()
