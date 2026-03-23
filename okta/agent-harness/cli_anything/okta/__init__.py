import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('okta running')
@cli.command()
def start(): click.echo('okta started')
if __name__ == '__main__': cli()
