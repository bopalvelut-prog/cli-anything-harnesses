import click
@click.group()
def cli(): pass
@cli.command()
def servers(): click.echo('Server stats')
@cli.command()
def traffic(): click.echo('Traffic stats')
if __name__ == '__main__': cli()
