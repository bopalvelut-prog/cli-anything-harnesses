import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('forgejo running')
@cli.command()
def start(): click.echo('forgejo started')
if __name__ == '__main__': cli()
