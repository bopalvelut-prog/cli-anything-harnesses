import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('snowflake running')
@cli.command()
def start(): click.echo('snowflake started')
if __name__ == '__main__': cli()
