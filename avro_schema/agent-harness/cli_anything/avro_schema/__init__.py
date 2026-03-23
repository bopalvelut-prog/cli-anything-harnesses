import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('avro_schema running')
@cli.command()
def start(): click.echo('avro_schema started')
if __name__ == '__main__': cli()
