import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('pod')
def logs(pod): subprocess.run(['stern', pod])
if __name__ == '__main__': cli()
