import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('avro running')
@cli.command()
def start(): click.echo('avro started')
if __name__ == '__main__': cli()
