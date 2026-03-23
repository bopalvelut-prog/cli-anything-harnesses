import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_data_pipeline running')
@cli.command()
def start(): click.echo('aws_data_pipeline started')
if __name__ == '__main__': cli()
