import click
@click.group()
def cli(): pass
@cli.command()
def instances(): click.echo('Spanner instances')
@cli.command()
def databases(): click.echo('Spanner databases')
if __name__ == '__main__': cli()
